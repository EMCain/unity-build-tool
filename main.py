import subprocess
import os

def run(cmd):
    completed = subprocess.run(['Powershell', '-Command', cmd], capture_output=True)
    return completed

def get_path():
    current = os.getcwd()
    user_defined = input(f'Enter folder to output to ({current})').strip()
    if (len(user_defined) == 0):
        return current
    return user_defined

def get_platform_folder_names(game_name, version):
    for platform_name in ['Windows', 'Mac', 'Web']:
        yield f'{game_name}-{platform_name}-{version}'

def get_output_folder_name(base_path):
    default_game_name = os.path.basename(base_path)
    game_name = input(f'Enter game name: ({default_game_name})').strip()
    version = input('Enter version number: ').strip()
    while len(version) == 0:
        version = input('Must enter version number e.g. 1.0.0: ').strip()
    
    if len(game_name) == 0:
        game_name = default_game_name

    return f'{game_name}-{version}'

def create_version_build(output_path, version_and_game_name, platform_name):
    version_build_name = f'{version_and_game_name}-{platform_name}'
    print(f'Creating build for {platform_name} at {version_build_name}')
    os.mkdir(os.path.join(output_path, version_build_name))
    print(f'TODO create build for {platform_name}')

if __name__ == '__main__':
    print('Starting build; hit "enter" to use (default)')
    base_path = get_path()
    builds_path = os.path.join(base_path, 'Builds')
    base_items = os.listdir(base_path)

    if ('Builds' not in base_items):
        print('creating "Builds" folder...')
        os.mkdir(builds_path)
    
    build_items = os.listdir(builds_path)
    print(f'Existing builds: {build_items}')

    output_folder_name = get_output_folder_name(base_path)

    while output_folder_name in build_items:
        print(f'Folder "{output_folder_name}" already exists in directory "{builds_path}". Delete it or pick new name/version')
        output_folder_name = get_output_folder_name(base_path)
    
    print(f'Creating output folder at ${output_folder_name}...')
    output_folder_path = os.path.join(builds_path, output_folder_name)
    os.mkdir(output_folder_path)

    for platform_name in ['Windows', 'Mac', 'Web']:
        create_version_build(output_folder_path, output_folder_name, platform_name)
    


# # https://www.phillipsj.net/posts/executing-powershell-from-python/
# if __name__ == '__main__':
#     hello_command = 'Write-Host "Hello World!"'
#     hello_info = run(hello_command)
#     if hello_info.returncode != 0:
#         print('An error occurred: %s', hello_info.stderr)
#     else: 
#         print('Hello command executed successfully!')

#     print('----------------')

#     bad_syntax_command = 'Write-Hsttt "bad syntax command"'
#     bad_syntax_info = run(bad_syntax_command)
#     if bad_syntax_info.returncode != 0:
#         print('an error occurred: %s', bad_syntax_info.stderr)
#     else: 
#         print('run successfully')