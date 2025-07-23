require 'set'
require 'asciidoctor'
require 'yaml'

def get_files(dir, *patterns)
  patterns
    .flat_map { |pattern| Dir.glob(File.join(dir, pattern)) }
    .map { |path| File.expand_path(path, dir) }
    .to_set
end

def get_adoc_files(dir)
  get_files(dir, '**/*.adoc')
end

def get_snippets(dir)
  get_files(dir, 'snippets/*.adoc', 'snippets/*.yaml')
end

def get_modules(dir)
  get_files(dir, 'modules/*.adoc')
end

def get_topic_maps(dir)
  get_files(dir, '_topic_maps/*.yml')
end

def extract_topic_map_paths(data, base_path)
  paths = []

  data.each do |section|
    next unless section['Dir'] && section['Topics']

    group_dir = File.join(base_path, section['Dir'])

    section['Topics'].each do |topic|
      if topic['File']
        paths << File.join(group_dir, "#{topic['File']}.adoc")
      elsif topic['Dir'] && topic['Topics']
        paths.concat(extract_topic_map_paths([topic], group_dir))
      end
    end
  end

  paths
end


def extract_used_files(file_path)
    doc = nil
    begin
      doc = Asciidoctor.load_file file_path, safe: :unsafe, sourcemap: true
    rescue Errno::ENOENT => e
      puts "Error: The file '#{file_path}' was not found or could not be read. Details: #{e.message}"
      return nil
    rescue Asciidoctor::SyntaxError => e
      puts "Error: Invalid AsciiDoc syntax in '#{file_path}'. Details: #{e.message}"
      return nil
    rescue StandardError => e
      puts "An unexpected error occurred: #{e.message}"
      puts e.backtrace.join("\n")
      return nil
    end

    used_file_locations = Set.new
    if doc
        whole_docs = doc.find_by
        whole_docs.each do |element|
            if element.file
                begin
                    real_path = File.realpath(element.file)
                    used_file_locations.add(real_path)
                rescue Errno::ENOENT => e
                    puts "Warning: Included file via symlink '#{element.file}' resolves to a non-existent path. Details: #{e.message}"
                rescue StandardError => e
                    puts "Warning: Could not resolve real path for '#{element.file}'. Details: #{e.message}"
                    used_file_locations.add(element.file)
                end
            end
        end
    end
    return used_file_locations
end

def compare_present_with_used(used_files, project_root)
#     present_files = get_modules(project_root) + get_snippets(project_root)
# FIXME: Oh, duh. Snippets can be used in modules.
    present_files = get_modules(project_root)
    return present_files - used_files
end

def main
    # TODO: Don't hardcode project root. 
    project_root = '/home/ahoffer/git/openshift-docs'
    topic_map_files = get_topic_maps(project_root)

    full_paths = topic_map_files.flat_map do |file|
      topic_map_data = YAML.load_stream(File.read(file))
      extract_topic_map_paths(topic_map_data, project_root)
    end

    used_files = Set.new

    full_paths.each do |path|
      files = extract_used_files(path)
      used_files.merge(files) if files
    end

    results = compare_present_with_used(used_files, project_root)
    pp results
    puts results.length
    puts "WIP: So far, modules only!"
end

if __FILE__ == $0
  main
end
    # NOTE: Look at tally method for reporting
