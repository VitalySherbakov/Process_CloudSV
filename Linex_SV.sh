versionscript=1.010
echo "Установка и Работа Process_Cloud SV (Щ.В) (v $versionscript)"
distributivelinex=$(lsb_release -is)
numberversionlinex=$(lsb_release -rs)

function main(){
    echo "Команда: pack (Установка необходимых пакетов)"
	echo "Команда: exit (Выход)"
	echo "Введите Команду:"
	read command
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