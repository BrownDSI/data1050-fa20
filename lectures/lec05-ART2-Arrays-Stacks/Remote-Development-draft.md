# Remote Development

## TCP/IP
Connections between machines can be established using various physical mechanisms (e.g., electrical, wifi, optical) and a vast number of protocols.

The [Internet Protocol Suite](https://en.wikipedia.org/wiki/Internet_protocol_suite) (aka TCP/IP) defines a set of communications protocols for transferring data back and forth between programs running on machines on the same physical network, and also across the Internet.  The essential idea is that information could be digitally encoded and sent via "packets" of data.

TCP/IP protocols define where and how these packets are transferred.  

## Background
The origins and history of the Internet are fascinating and relevant to DATA1050.  The US military-funded development of  TCP/IP to deploy a private version of the Internet called ARPANET. ARPANET's original intent was to allow remote users to share access to large computer systems for scientific computing.  However, heterogeneity in the systems (every manufacturer had a different approach to how its machines were programmed) and end-user compute environments, meant that the system wasn't very effective, and ARPANET wasn't viewed as a success.

Today, things have improved a lot. We have vastly more amounts of standardization, including protocols for the representation, manipulation, and display of information.

Also, as a personal historical note, there were many other networked systems at the time of the ARPANET; some were dedicated to education, including [PLATO](https://www.amazon.com/Friendly-Orange-Glow-Untold-Cyberculture/dp/1101871555). Using that system, while an early teen, I wrote and used many interactive graphical programs, including ones that used touch screens and multi-player/multi-user games - all in the late 1970s and early 1980s. At that time, ARPANET only supported the use of teletype style terminals.

## Connections
Thus far, in DATA1050, we've been working with our Google Cloud Shell's through its web interface via the [https](https://en.wikipedia.org/wiki/HTTPS) protocol.  

Most Data Systems also allow for non-browser-based connections to facilitate communication with their underlying services. A common way to secure these connections is by encrypting them via [Ssh (Secure Shell)](https://en.wikipedia.org/wiki/Ssh_(Secure_Shell)).  You may have already used to Ssh to login and access a command line on a remote machine.  However, Ssh can be used to secure *any* [network service](https://en.wikipedia.org/wiki/Ssh_(Secure_Shell)).  

During your career as a Data Scientist, you'll encrypt all manner of connections with Ssh.

For today, we're going to use Ssh to connect to our cloud shell in three ways:

1. Directly, by logging into a Bash session
2. Through tunneling, to access a web server running on your Cloud Shell
3. Via VSCode to do remote development work

## GCloud Specific Setup
The platform management functionality provided by Google Cloud Shell can be also be done on your local machine via the Google [Cloud SDK](https://cloud.google.com/sdk).  Please download and install a copy now.

After your installation is complete, run 'gcloud init' and answer yes to the login prompt.  

You can connect to a terminal shell running on your gcloud shell using Ssh encryption via the following command.

`$ gcloud alpha cloud-shell ssh`

Please try this now. It should look familiar! You can close the connection using by typing exit.  [glcloud alpha cloud-shell](https://cloud.google.com/sdk/gcloud/reference/alpha/cloud-shell) also lets you efficiently copy files between your local machine and on your cloud-shell via 'scp'.  You can even mount your cloud-shell using the 'get-mounted-command'.

Since both ssh and scp are common commands, rather than learn a google specific approach to using them, we'll use focus on using them in the usual way.

In order to do this, we need to provide local access to the ssh network-service running on your cloud-shell.

Hmmm, how can we make a secure connection to a network service? Why Ssh, of course! Executing the following command in your local shell


`$ gcloud alpha cloud-shell ssh --ssh-flag='-L 6000:127.0.0.1:22'`

This exposes the default ssh port on your Gcloud machine to port 6000 on your local machine. Data exchanged via 127.0.0.1:6000 locally will now be securely tunneled back and forth with port 22 on your remote cloud machine. (On many systems, `localhost` is available for 127.0.0.1, and it might be easier for you to remember.)

## Ssh Remote logon

The standard way to connect to a terminal window on a remote machine is via
`$ ssh hostname'

Since we have exposed the remote Ssh locally on port 6000, the command you will use to get to your cloud shell is

`ssh -p 6000 daniel_potter@127.0.0.1 -i ~/.ssh/google_compute_engine`

Be sure to replace my login with your login name; please confirm that this is working for you now.  The last part of the command indicates which Ssh password keys to use.  

## Ssh Tunneling

We already saw one example of tunneling when we exposed remote port 22 on local port 6000.  We can do this again to map some other ports, for example 

`ssh -p 6000 -L8888:127.0.0.1:8888 daniel_potter@127.0.0.1`

Will map port 8888 from your cloud-shell to your local machine's port 8888. 

Try firing up Jupyter Lab or Jupyter Notebook on your cloud-shell by running

`$ jupyter lab`

and visiting [https:\\127.0.0.1:8888](https:\\127.0.0.1:9999) in your browser. (The default port for Jupyter Notebook and Jupyer Lab is port 8888, but you can adjust this is you want to run multiple copies at once.)

Note: You can install jupyter lab via `conda install jupyterlab`

## Remote Development with VS Code

### Open VS Code and install the following extensions:
1. [MS python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
2. [MS Remote Development](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack)

The MS [Remote Development](https://code.visualstudio.com/docs/remote/ssh) is fantastic. 

Using the `Remote-SSH: Connect to Host...`>`Configure SSH Hosts...` 

Add a block that looks like the following, except with your details:

```
Host cloud-shell
    Port 6000
    #ForwardAgent yes
    HostName localhost
    User daniel_potter
    IdentityFile ~/.ssh/google_compute_engine
```

