#!/bin/bash

# Solicitar el nombre del archivo de entrada
read -p "Ingrese el nombre del archivo de entrada: " input_file

# Verificar si el archivo de entrada existe
if [ ! -f "$input_file" ]; then
  echo "El archivo de entrada no existe. Saliendo."
  exit 1
fi

# Solicitar el nombre del archivo de salida
read -p "Ingrese el nombre del archivo de salida: " output_file

# Comienza el archivo JSON
echo "{" > "$output_file"
echo '  "hostnames": [' >> "$output_file"

# Leer cada línea del archivo de entrada
first=true
while IFS=" " read -r ip port domain; do
  # Comprobar si el primer campo (IP) es válido
  if [[ "$ip" =~ ^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$ ]] && [[ "$port" =~ ^[0-9]+$ ]]; then
    # Si no es la primera línea, agrega una coma al final de la línea anterior
    if [ "$first" = true ]; then
      first=false
    else
      echo "," >> "$output_file"
    fi
    # Agregar la línea al archivo JSON
    echo "    {\"ip\": \"$ip\", \"port\": $port}" >> "$output_file"
  elif [[ "$ip" =~ ^[a-zA-Z0-9.-]+$ ]] && [[ "$port" =~ ^[0-9]+$ ]]; then
    # Si es un dominio, agregarlo de manera similar a la IP
    if [ "$first" = true ]; then
      first=false
    else
      echo "," >> "$output_file"
    fi
    echo "    {\"ip\": \"$ip\", \"port\": $port}" >> "$output_file"
  fi
done < "$input_file"

# Cierra el array y el objeto JSON
echo "  ]" >> "$output_file"
echo "}" >> "$output_file"

echo "Archivo JSON generado: $output_file"
