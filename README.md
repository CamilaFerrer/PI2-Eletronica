# Projeto Integrador 2


## Configurando conexão VNC da Raspberry Pi 3 (Raspbian) com Desktop/Laptop (Linux)

### Configurando Raspberry

A conexão VNC já está incluída no Raspbian, mas é necessário habilitá-la.

Caso tenha uma versão anterior do Raspbian ou uma distribuição diferente do Linux, instale a conexão VNC manualmente. Primeiramente, execute os comandos abaixo para garantir que tenha a versão mais atualizada do VNC Server:

```
sudo apt-get update
sudo apt-get install realvnc-vnc-server 
```

Caso esteja utilizando uma versão antiga do VNC Server, [reinicie o programa](https://www.realvnc.com/pt/connect/docs/raspberry-pi.html#raspberry-pi-ssh).

Caso não esteja, vá em **Menu > Preferences > Raspberry Pi Configuration > Interfaces** e habilite o VNC marcando **Enabled**. Se quiser fazer pela linha de comando, execute ``sudo raspi-config``, vá até **Interfacing Options > VNC** e selecione **Yes**.

A partir de agora, seu VNC Server começará automaticamente sempre que você ligar sua Raspberry Pi.

### Configurando Desktop/Laptop

Faça download do arquivo .deb correspondente a sua versão de Sistema Operacional no site [RealVNC Viewer](https://www.realvnc.com/en/connect/download/viewer/) e mova o arquivo baixado para sua pasta pessoal. No terminal, execute os comandos:

```
sudo dpkg -i <filename>
sudo apt-get install -f
```

Substitua <filename> pelo nome do arquivo que você baixou (VNC-Viewer-version-number.deb).


## Conexão VNC por nuvem

Cloud connections are convenient and encrypted end-to-end, and highly recommended for connections over the Internet. There’s no firewall or router reconfiguration, and you don’t need to know the IP address of your Raspberry Pi, or provide a static one.

You’ll need a RealVNC account; it’s completely free to set up and only takes a few seconds. We’ll give you a special version of our Home subscription that enables both cloud and direct connectivity, and also in-session features such as system authentication, file transfer, printing and chat.

You can apply your Home subscription to five Raspberry Pis and/or desktop computers in total. Please note you revert to the standard feature set for Windows, Mac and Linux desktop computers.

Sign up for a RealVNC account by entering your email address in the box on this page, and following the instructions.

On your Raspberry Pi, select Licensing from the VNC Server status menu, choose Sign in to your RealVNC account, and enter your new account email and password:

On the device you will use to take control, run VNC Viewer and sign in using the same account credentials.

In VNC Viewer, a connection to your Raspberry Pi automatically appears under the name of your team. Simply tap or double-click to connect:

Authenticating to VNC Server
To complete either a direct or cloud connection you must authenticate to VNC Server. Enter the user name and password you normally use to log on to your user account on the Raspberry Pi.

By default, these credentials are pi and raspberry, but hopefully you’ll have changed them to something more secure by now!

Para mais informações acesse [aqui](https://www.realvnc.com/pt/connect/docs/raspberry-pi.html).

## Conexão VNC por cabo de ethernet

Assuming your Internet connection is on Wi-Fi, and you want to share via cable. On Ubuntu 14.04 open Network connections from the applet or via commandline nm-connection-editor, then add a connection, select type ethernet, create, then on tab IPv4 Settings select Method Shared to other computers. That should be all for connection sharing.

https://help.ubuntu.com/community/Internet/ConnectionSharing


https://www.dexterindustries.com/howto/virtually-control-the-raspberry-pi/


Establishing a direct connection
Direct connections are quick and simple providing you’re joined to the same private local network as your Raspberry Pi (for example, a wired or Wi-Fi network at home, school or in the office).

If you’re connecting over the Internet, it’s much safer and more convenient to establish a cloud connection.

On your Raspberry Pi, discover its private IP address by double-clicking the VNC Server icon on the taskbar and examining the status dialog:

On the device you will use to take control, run VNC Viewer and enter the IP address in the search bar:


