versionscript=1.010
echo "Установка и Работа Process_Cloud SV (Щ.В) (v $versionscript)"
distributivelinex=$(lsb_release -is)
numberversionlinex=$(lsb_release -rs)
dirsource="Process_CloudSV"

function python_run(){
	# Запуск Скрипта
	nameuser=$USER
	#python="/home/$nameuser/Python-3.8.0/python"
	#$python "/home/$nameuser/$dirsource/$1.py" "linex"
	python3.8 "/home/$nameuser/$dirsource/$1.py" "linex"
}

function python_pip_list_libs(){
	# Список Библиотек pip
	nameuser=$USER
	#python="/home/$nameuser/Python-3.8.0/python"
	#$python "-m pip freeze" "linex"
	#python3.8 "-m pip freeze" "linex"
	pip freeze
}

function python_pip_update(){
	# Обновление pip
	#nameuser=$USER
	#python="/home/$nameuser/Python-3.8.0/python"
	#$python "-m pip install --upgrade pip" "linex"
	#python3.8 "-m pip install --upgrade pip" "linex"
	pip install --upgrade pip
}

function python_pip_install(){
	# Установка pip пакета
	nameuser=$USER
	#python="/home/$nameuser/Python-3.8.0/python"
	#$python "-m pip install $1" "linex"
	#python3.8 "-m pip install $1" "linex"
	pip install $1
}

function cd_set_home(){
	# Вернуться на Исходные Позиции
	nameuser=$USER
	cd "/home/$nameuser"
}

function update_mashine(){
	# Автообновления
	echo "Автообновление..."
	apt-get update -y && apt-get upgrade -y
}

function pip_install_python(){
	# Установка pip на python
	curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
	sudo python3.8 get-pip.py
}

function function_install_python(){
	# Установка Py 3.8.0
	update_mashine
	sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libsqlite3-dev libreadline-dev libffi-dev curl libbz2-dev
	wget https://www.python.org/ftp/python/3.8.0/Python-3.8.0.tgz
	tar -xf Python-3.8.0.tgz
	cd Python-3.8.0
	./configure --enable-optimizations
	make -j $(nproc)
	sudo make altinstall
	update_mashine
	pip_install_python
	python_pip_update
	python_pip_install requests
	python_pip_install alive-progress
	python_pip_install tqdm
	python_pip_install py7zr
	python_pip_install rarfile
	python3.8 --version
	cd_set_home
}

function function_pack10(){
	# Установка Пакетов
	update_mashine
	echo "Загрузка Пакетов 1..."
	apt-get install sudo -y
	sudo apt-get install ssh -y
	sudo apt-get install wget -y
	sudo apt-get install git -y
	update_mashine
	echo "Загрузка Пакетов 2..."
	function_install_python
	function_install_gpu
	function_install_cpu
	echo "Установка Пакетов Завершена!"
}

function main(){
	# Основное Меню
	echo "Конвентация *.cap в *.hc22000 по адресу https://hashcat.net/cap2hashcat/"
    echo "Команда: pack (Установка необходимых пакетов)"
	echo "Команда: list (Список пакетов)"
	echo "Команда: gpu_test (Проверка GPU)"
	echo "Команда: cpu_test (Проверка CPU)"
	echo "Команда: run (Запуск Скрипта)"
	echo "Команда: exit (Выход)"
	echo "Введите Команду:"
	read command
	if [ "$command" == "list" ]; then
		python_pip_list_libs
	fi
	if [ "$command" == "pack" ]; then
		function_pack10
	fi
	if [ "$command" == "gpu_test" ]; then
		function_run_gpu "--help"
	fi
	if [ "$command" == "cpu_test" ]; then
		function_run_cpu "--help"
	fi
	if [ "$command" == "run" ]; then
		python_run "Main"
	fi
	if [ "$command" == "exit" ]; then
		break
	fi
}

while true
do
	current_time=$(date +%d.%m.%Y\ %T) # тикущая дата
	echo "-------------------------$current_time--------------------------"
	if [ "$distributivelinex" == "Debian" ]; then
		echo "Линекс: $distributivelinex"
		if [ "$numberversionlinex" == 11 ]; then
			echo "Версия: $numberversionlinex"
            main
        fi
        if [ "$numberversionlinex" == 10 ]; then
            echo "Версия: $numberversionlinex"
            main
        fi
        if [ "$numberversionlinex" == 9 ]; then
			echo "Версия: $numberversionlinex"
			echo "Пока не доступно!"
		fi
    fi
	if [ "$distributivelinex" == "Ubuntu" ]; then
		echo "Линекс: $distributivelinex"
		echo "Пока не доступно!"
	fi
	read -p "Нажмите Enter, чтобы продолжить"
done