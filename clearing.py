
# import subprocess

# # Создаем список процессов, которые нужно убить
# process_names = ['Lively.exe', 'Rainmeter.exe', 'RoundedTB.exe', 'browser.exe']

# # Функция для вывода информации о свободной оперативной памяти
# def get_ram_usage():
    # return psutil.virtual_memory().available / 1024  *  *  3


# for process_name in process_names:
    # # Убиваем процесс
    # try:
        # subprocess.run(['taskkill', '/F', '/IM', process_name], check=False)
    # except Exception as e:
        # print(f'Ошибка при попытке убить процесс "{process_name}": {e}')
        
        
import psutil

def kill_processes_by_name(process_names):
    total_memory_freed = 0
    for proc in psutil.process_iter(['pid', 'name', 'memory_info']):
        try:
            if proc.info['name'] in process_names:
                memory_info = proc.info['memory_info'].rss
                proc.terminate()  # или proc.kill() для немедленного завершения
                proc.wait(timeout=3)  # ждем завершения процесса
                total_memory_freed += memory_info
                print(f"Процесс {proc.info['name']} (PID {proc.info['pid']}) завершен.")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.TimeoutExpired) as e:
            print(f"Не удалось завершить процесс {proc.info['name']} (PID {proc.info['pid']}): {e}")
    
    return total_memory_freed

def format_memory_size(bytes_size):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes_size < 1024:
            return f"{bytes_size:.2f} {unit}"
        bytes_size /= 1024

# Пример имен процессов, которые нужно завершить
process_names_to_kill = ['Lively.exe', 'Rainmeter.exe', 'RoundedTB.exe', 'browser.exe'] # замените на реальные имена процессов

while True:
    freed_memory = kill_processes_by_name(process_names_to_kill)
    formatted_memory = format_memory_size(freed_memory)
    print(f"Освобождено оперативной памяти: {formatted_memory}")
    user_input = input("e для выхода): ")
    if user_input.lower() == 'e':
        break
    

