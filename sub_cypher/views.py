from django.shortcuts import render, redirect
from sub_cypher.models import LogEntry
from venv import logger
from django.http import HttpResponse
from sub_cypher.forms import JumpForm
from rest_framework import generics
from sub_cypher.models import LogEntry
from sub_cypher.serializers import LogEntrySerializer


class LogEntryListCreateView(generics.ListCreateAPIView):
    queryset = LogEntry.objects.all()
    serializer_class = LogEntrySerializer

class LogEntryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LogEntry.objects.all()
    serializer_class = LogEntrySerializer


global jumps  # Use the global keyword to update the global variable 'jumps'

def instantiate(request):
     if request.method == 'POST':
        form = JumpForm(request.POST)
        if form.is_valid():
            jumps = form.cleaned_data['jumps']
            request.session['jumps'] = jumps
            return redirect('encrypt')
     else:
        form = JumpForm()
     return render(request, 'instantiate.html', {'form': form})

   
def encrypt(request):
    jumps = request.session.get('jumps', 0)
    if request.method == 'POST':
        plain_text = request.POST.get('plain_text', '')
        plainText = input('ENTER MESSAGE: ')
        key = jumps  
        ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
        cypherText = ' '

        for letter in plainText:
            if letter.lower() in ALPHABET:
                num = ALPHABET.find(letter.lower())
                num = (num + key) % len(ALPHABET)  # Use modulo to handle wrapping around the alphabet
            if letter == letter.lower():
                cypherText += ALPHABET[num]
            else:
                cypherText += ALPHABET[num].upper()
        else:
            cypherText += letter
        print(cypherText)
        log_entry = LogEntry(operation='encryption', original_text=plain_text, result_text=cypher_text)
        log_entry.save()
    else:
        cypher_text = ''
    return render(request, 'encrypt.html', {'cypher_text': cypher_text})

def decrypt(request):
    jumps = request.session.get('jumps', 0)
    if request.method == 'POST':
        cypher_text = request.POST.get('cypher_text', '')
        plainText = input('ENTER MESSAGE: ')
        key = jumps  # Use the global 'jumps' variable as the decryption key
        ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
        cypherText = ' '

        for letter in plainText:
            if letter.lower() in ALPHABET:
                num = ALPHABET.find(letter.lower())
                num = (num - key) % len(ALPHABET)  # Use modulo to handle wrapping around the alphabet
                if letter == letter.lower():
                    cypherText += ALPHABET[num]
                else:
                    cypherText += ALPHABET[num].upper()
            else:
                cypherText += letter
        print(cypherText)
        log_entry = LogEntry(operation='decryption', original_text=cypher_text, result_text=plain_text)
        log_entry.save()
    else:
        plain_text = ''
    return render(request, 'decrypt.html', {'plain_text': plain_text})



def history(request):
    log_entries = LogEntry.objects.all()
    return render(request, 'history.html', {'log_entries': log_entries})


def menu(request):
    choice = " "

    # To display a menu
    while (choice.lower() != "0"):
        print('''
        1. Instantiate encryption parameters
        2. Encrypt text
        3. Decrypt text
        4. Reset encryption parameters
        5. History
        ''')

        print("Enter the number that corresponds with the task you want to perform: ")
        choice = input()

        if choice == "1":
            jumps = instantiate()
            print(f'jumps instantiated to {jumps}')
            input("Press Enter to continue...")

        elif choice == "2":
            encrypt()
            input("Press Enter to continue...")

        elif choice == "3":
            decrypt()
            input("Press Enter to continue...")

        elif choice == "0":
            print("Exit")
            return render(request, 'exit.html')

        elif choice == "4":
            jumps = 0
            print("Restarting...")
            print("Enter new encryption parameters")
            input("Press Enter to continue...")

        elif choice == "5":
            history()

        else:
            print("The feature has not been implemented yet, please check back for updates.")

    return render(request, 'menu.html')
 #logger.addLog(f'encryption - {plainText} - {cypherText}')
 #cypher_text = encrypt_text(plain_text, jumps)  # Implement the encryption logic
 #logger.addLog(f'decryption - {plainText} - {cypherText}')
 #plain_text = decrypt_text(cypher_text, jumps)  # Implement the decryption logic