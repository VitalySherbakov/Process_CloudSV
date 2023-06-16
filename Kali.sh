versionscript=1.012
echo "Установка и Работа Process_Cloud SV (Щ.В) (v $versionscript)"
distributivelinex=$(lsb_release -is)
numberversionlinex=$(lsb_release -rs)
dirsource="Process_CloudSV"

function update_mashine(){
	# Автообновления
	echo "Автообновление..."
	apt-get upgrade openssl -y && apt-get update -y && apt-get upgrade -y
}

function libs_all(){
    # Пакеты Компиляции
    sudo apt-get install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libnl-3-dev libnl-genl-3-dev pkg-config libsqlite3-dev libpcre3-dev libffi-dev curl libreadline-dev ethtool libbz2-dev libtool autoconf -y
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
    apt install aircrack-ng -y
	aircrack-ng --help
	cd ..
}

function function_install_gpu(){
	# Установка GPU
	update_mashine
	cd "$dirsource"
	git clone "https://github.com/VitalySherbakov/hashcat"
	sudo apt install cmake build-essential -y && apt install checkinstall git -y && cd hashcat && git submodule update --init && make && make install
	update_mashine
	hashcat --help
	cd ..
}

function function_pack10(){
    # Установка Пакетов
    update_mashine
    libs_all
    chmod -R 777 "$dirsource/"
    chmod +x "$dirsource/"
	echo "Загрузка Пакетов 1..."
	apt-get install sudo -y
	sudo apt-get install ssh -y
	sudo apt-get install wget -y
	sudo apt-get install git -y
	sudo apt-get install p7zip-full -y
	sudo apt-get install unrar-free -y
	update_mashine
	echo "Загрузка Пакетов 2..."
    #python -m pip install requests
	python -m pip install alive-progress
	python -m pip install tqdm
	python -m pip install py7zr
	python -m pip install rarfile
    #python -m pip install urllib3==1.26.7
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
        python "./$dirsource/Kali.py" "$1"
	fi
    if [ "$command" == "exit" ]; then
		break
	fi
}

while true
do
    current_time=$(date +%d.%m.%Y\ %T) # тикущая дата
    echo "-------------------------$current_time--------------------------"
    echo "Платформа: $distributivelinex"
    echo "Версия: $numberversionlinex"
    if [ "$distributivelinex" == "Kali" ]; then
        main "$distributivelinex"
    fi
    read -p "Нажмите Enter, чтобы продолжить"
done