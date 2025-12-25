from datetime import datetime
message = "Error en red"
date = datetime.now().strftime( "%d/%m/%Y, %H:%M:%S")
with open("logs.txt","a") as log:
    log.write(f"[{date}] {message}\n")