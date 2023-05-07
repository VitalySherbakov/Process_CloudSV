versionscript=1.010
echo "Установка и Работа Process_Cloud SV (Щ.В) (v $versionscript)"
distributivelinex=$(lsb_release -is)
numberversionlinex=$(lsb_release -rs)

function function_install_python(){
	sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev
	echo "Автообновление..."
	apt-get update -y
	apt-get upgrade -y
	wget https://www.python.org/ftp/python/3.8.0/Python-3.8.0.tgz
	tar -xf Python-3.8.0.tgz
	rm -r Python-3.8.0.tgz
	cd Python-3.8.0
	./configure --enable-optimizations
	make -j $(nproc)
	sudo make altinstall
	python3.8 --version
}

function function_pack10(){
	echo "Автообновление..."
	apt-get update -y
	apt-get upgrade -y
	echo "Загрузка Пакетов 1..."
	apt-get install sudo -y
	sudo apt-get install ssh -y
	sudo apt-get install wget -y
	sudo apt-get install git -y
	echo "Автообновление..."
	apt-get update -y
	apt-get upgrade -y
	echo "Загрузка Пакетов 2..."
	function_install_python
	echo "Установка Пакетов Завершена!"
}

function main(){
    echo "Команда: pack (Установка необходимых пакетов)"
	echo "Команда: exit (Выход)"
	echo "Введите Команду:"
	read command
	if [ "$command" == "pack" ]; then
		function_pack10
	fi
	if [ "$command" == "exit" ]; then
		break
	fi
}

while true
do
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