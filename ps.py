import subprocess

def run(cmd):
    completed = subprocess.run(['Powershell', '-Command', cmd], capture_output=True)
    return completed

# https://www.phillipsj.net/posts/executing-powershell-from-python/
if __name__ == '__main__':
    hello_command = 'Write-Host "Hello World!"'
    hello_info = run(hello_command)
    if hello_info.returncode != 0:
        print('An error occurred: %s', hello_info.stderr)
    else: 
        print('Hello command executed successfully!')

    print('----------------')

