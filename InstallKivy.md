# Install Kivy

Before installing Kivy, we need to create an environment. Use the following command to create a new environment called kivy:
~~~
conda create -n kivy python=3.4
~~~

Once created, you can activate it with the following command:
~~~
activate kivy
~~~

With this environment active, you can install Kivy using the following command:
~~~
pip install kivy kivy.deps.glew kivy.deps.sdl2 pygments
~~~

Note, that whenever you want to use Kivy, you must switch into the kivy environment. One way to do this automatically is to create a shortcut. First find and copy your Anaconda prompt shortcut. Then rename it to Kivy prompt. Open the properties, and change the Target line by replacing the path after activate.bat with kivy.
