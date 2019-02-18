# Projeto Integrador 2

## Objetivo

Desenvolvimento de um robô que realiza a limpeza de locais arenosos, como parques infantis e quadras de esporte, de forma autônoma. A limpeza será focada em pequenos objetos que são mais comuns nesse tipo de ambiente como: resto de comida, embalagens plásticas, pedras maiores, galhos de árvores, folhas, etc. Além de proporcionar aos usuário um mapeamento das áreas que apresentam estados mais críticos para que possam ser aplicadas políticas de fiscalização mais eficientes.

## Equipe de Eletrônica

A equipe trabalhará com a definições de sensores, processamento de sinais dos sensores, automatização e comunicação.

|       Nome       |              Papel            |                               Responsabilidades                            |
|:----------------:|:-----------------------------:|:--------------------------------------------------------------------------:|
| Alexandre Santos | Desenvolvedor                                           | Desenvolvimento dos recursos e artefatos do<br> subprojeto de eletrônica, apoia integração dos<br> outros subprojetos                                       |
| Camila Ferrer    | Gerente do Projeto<br>Gerente de Eletrônica<br>Desenvolvedora | Gerenciar a equipe do projeto e a de eletrônica,<br> desenvolvimento dos recursos e artefatos deste<br> subprojeto, apoia integração dos outros subprojetos |
| Edilberto Abraão | Desenvolvedor                                           | Desenvolvimento dos recursos e artefatos do<br> subprojeto de eletrônica, apoia integração dos<br> outros subprojetos                                       |
| Jéssica Souza    | Desenvolvedor                                           | Desenvolvimento dos recursos e artefatos do<br> subprojeto de eletrônica, apoia integração dos<br> outros subprojetos                                       |


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

Conexão por nuvem é conveniente, segura, não necessita de um firewall ou reconfigurar seu roteador e não é necessário saber o endereço IP da sua Raspberry Pi ou configurar um IP estático. Primeiramente, é necessário criar uma conta gratuita na RealVNC que permite conecxão por nuvem e direta.

Na sua Raspberry Pi, entre no Real VNC Server e acesse sua conta da RealVNC e, no dispositivo que será utilizado para controle da conexão, entre no Real VNC Viewer e também acesse sua conta. No VNC Viewer irá aparecer uma conexão automática com sua Raspberry Pi e basta clicar duas vezes para iniciar a conexão.

O VNC Server irá solicitar que você autentifique a conexão inserindo o nome de usuário e senha configurados na sua Raspberry Pi. O usuário padrão da Raspberry é _pi_ e a senha é _raspberry_, porém é aconselhavel mudar para uma senha mais segura assim que possível.

Para mais informações acesse [aqui](https://www.realvnc.com/pt/connect/docs/raspberry-pi.html).

## Conexão VNC por cabo de ethernet

Assuming your Internet connection is on Wi-Fi, and you want to share via cable. On Ubuntu 14.04 open Network connections from the applet or via commandline nm-connection-editor, then add a connection, select type ethernet, create, then on tab IPv4 Settings select Method Shared to other computers. That should be all for connection sharing.

https://help.ubuntu.com/community/Internet/ConnectionSharing

https://www.dexterindustries.com/howto/virtually-control-the-raspberry-pi/

Establishing a direct connection
Direct connections are quick and simple providing you’re joined to the same private local network as your Raspberry Pi (for example, a wired or Wi-Fi network at home, school or in the office).

If you’re connecting over the Internet, it’s much safer and more convenient to establish a cloud connection.

On your Raspberry Pi, discover its private IP address by double-clicking the VNC Server icon on the taskbar and examining the status dialog:

On the device you will use to take control, run VNC Viewer and enter the IP address in the search bar.

