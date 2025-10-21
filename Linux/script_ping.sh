
#!/bin/bash

HOST="8.8.8.8"
fail_count=0

while true; do
    ping_result=$(ping -c 1 -W 1 "$HOST" 2>/dev/null)
    current_time=$(date "+%Y-%m-%d %H:%M:%S")
    
    if [[ $ping_result == *"1 received"* ]]; then

	    fail_count=0 

	    time_ms=$(echo "$ping_result" | grep "time=" | awk -F "time=" '{print $2}' | awk '{print int($1)}')
	    time=$(echo "$ping_result" | grep "time=" | awk -F "time=" '{print $2}')

        
	    if (( $time_ms > 100 )); then

            echo "[$current_time] Высокая задержка: $time  (превышает 100 мс)"

        else

            echo "[$current_time] Пингуется нормально: $time "

        fi
        
    else

        ((fail_count++))
        
	if (($fail_count > 3)); then
            
                echo "больше трех неудачных попыток. $HOST -не работает"
           
	fi
    fi

    sleep 1
done
