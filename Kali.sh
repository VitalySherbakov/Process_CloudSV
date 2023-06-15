versionscript=1.012
echo "Установка и Работа Process_Cloud SV (Щ.В) (v $versionscript)"
distributivelinex=$(lsb_release -is)
numberversionlinex=$(lsb_release -rs)
dirsource="Process_CloudSV"



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
        python3.8 "./$dirsource/Linex_Main2.py" "$1"
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
    if [ "$distributivelinex" == "Ubuntu" ]; then
        access_ubuntu
        main "$distributivelinex"
    fi
    read -p "Нажмите Enter, чтобы продолжить"
done