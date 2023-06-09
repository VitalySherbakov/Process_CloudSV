versionscript=1.012
echo "Установка и Работа Process_Cloud SV (Щ.В) (v $versionscript)"
distributivelinex=$(lsb_release -is)
numberversionlinex=$(lsb_release -rs)
dirsource="Process_CloudSV"

function pip_install_python(){
	# Установка pip на python
	curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
	sudo python3.8 get-pip.py
}

function access_ubuntu(){
	# Ubuntu полный доступ к папке
	nameuser=$USER
	chmod -R 777 "/home/$nameuser/$dirsource/"
}

function update_mashine(){
	# Автообновления
	echo "Автообновление..."
	apt-get update -y && apt-get upgrade -y
}

function cd_set_home(){
	# Вернуться на Исходные Позиции
	nameuser=$USER
	cd "/home/$nameuser"
}

function function_install_cpu(){
	# Установка CPU
	update_mashine
	git clone https://github.com/aircrack-ng/aircrack-ng
    cd aircrack-ng
    bash "./autogen.sh"
    "./configure"
    make
    sudo make install
	update_mashine
	aircrack-ng --help
	cd_set_home
}

function function_install_gpu(){
	# Установка GPU
	update_mashine
	cd "$dirsource"
	git clone "https://github.com/VitalySherbakov/hashcat"
	sudo apt install cmake build-essential -y && apt install checkinstall git -y && cd hashcat && git submodule update --init && make && make install
	update_mashine
	hashcat --help
	cd_set_home
}

function function_install_python(){
	# Установка Py 3.8.0
	update_mashine
	sudo apt-get install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libnl-3-dev libnl-genl-3-dev pkg-config libsqlite3-dev libpcre3-dev libffi-dev curl libreadline-dev ethtool libbz2-dev libtool autoconf -y
	wget https://www.python.org/ftp/python/3.8.0/Python-3.8.0.tgz
	tar -xf Python-3.8.0.tgz
	rm -r Python-3.8.0.tgz
	cd Python-3.8.0
	./configure --enable-optimizations
	make -j $(nproc)
	sudo make altinstall
	update_mashine
	pip_install_python
	pip install --upgrade pip
	python3.8 --version
	curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
	sudo python3.8 get-pip.py
	pip install requests
	pip install alive-progress
	pip install tqdm
	pip install py7zr
	pip install rarfile
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
	sudo apt-get install p7zip-full -y
	sudo apt-get install unrar-free -y
	update_mashine
	echo "Загрузка Пакетов 2..."
	function_install_python
    function_install_cpu
    function_install_gpu
    echo "Установка Пакетов Завершена!"
}

function main(){
    # Основное Меню
    echo "Конвентация *.cap в *.hc22000 по адресу https://hashcat.net/cap2hashcat/"
    echo "Команда: pack (Установка необходимых пакетов)"
    echo "Команда: run (Запуск Скрипта)"
    echo "Команда: exit (Выход)"
    echo "Введите Команду:"
    read command
    if [ "$command" == "pack" ]; then
		function_pack10
	fi
    if [ "$command" == "run" ]; then
		python_run "Linex_Main" "$1"
	fi
    if [ "$command" == "exit" ]; then
		break
	fi
}

while true
do
    current_time=$(date +%d.%m.%Y\ %T) # тикущая дата
    echo "-------------------------$current_time--------------------------"
    if [ "$distributivelinex" == "Ubuntu" ]; then
        access_ubuntu
        echo "Линекс: $distributivelinex"
        main "$distributivelinex"
    fi
    read -p "Нажмите Enter, чтобы продолжить"
done