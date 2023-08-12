.. _doc_creating_settings_menus:

Creating settings menus
=======================

In a game project, it's essential for the player to be able to adjust settings.
This can be to match their hardware performance, or to suit their preferred
input configuration.

Changing settings at runtime
----------------------------

Most project settings are only read when the project starts. This means that to
change settings without having to restart the project, you have to find the
equivalent method that will change the setting at runtime.

For example, most rendering properties can be adjusted at runtime using the
:ref:`class_RenderingServer` methods listed in each project setting's
description. Likewise, audio properties can be adjusted by setting properties
and calling methods on the :ref:`class_AudioServer` singleton.

Changing settings that require a restart
----------------------------------------

If you change a project setting, it will usually only be applied after the
project is restarted. This poses the question: how is it possible to change a
project setting, since setting it in ``_ready()`` in an autoload will not have
any effect?

The answer is to use Godot's *project settings override* functionality. Any
project setting can be overridden by creating a file named ``override.cfg`` in
the project's root directory. This can also be used in exported projects by
placing this file in the same directory as the project binary. Overriding will
still take the base project settings' :ref:`feature tags <doc_feature_tags>` in
account. Therefore, make sure to *also* override the setting with the desired
feature tags if you want them to override base project settings on all platforms
and configurations.

You can change the path of the project settings override file by modifying
:ref:`application/config/project_settings_override
<class_ProjectSettings_property_application/config/project_settings_override>`
in the Project Settings.

.. tip::

    You can restart the project by calling :ref:`OS.set_restart_on_exit
    <class_OS_method_set_restart_on_exit>` with ``true`` as a parameter, then
    exiting the project using ``get_tree().quit()``. This can be useful to
    provide a button for users to restart the project after changing a setting
    that requires a restart to be effective. See :ref:`doc_handling_quit_requests`
    for more information.

Types of settings
-----------------


Graphics settings
^^^^^^^^^^^^^^^^^

Audio settings
^^^^^^^^^^^^^^

Input settings
^^^^^^^^^^^^^^

Game settings
^^^^^^^^^^^^^

It's advised to set these properties in an :ref:`autoload <doc_singletons_autoload>`, so that you can query them from anywhere easily.

Alternatively, you can choose to create custom project settings using ``ProjectSettings.set_setting("path/to/setting", value)``, but this won't provide type safety when querying the value.

Accessibility settings
^^^^^^^^^^^^^^^^^^^^^^

To make your game accessible to pl

Exposing an UI scale option

For specific UI elements such as subtitles, it's also worth exposing a font size setting. This can be done by having modifying a Theme resource's font size, then using this Theme resource for all elements where the font size should be changed:


Godot provides :ref:`text-to-speech <doc_text_to_speech>` functionality, which
can be useful to expose as an option. For example, in a multiplayer game, you
could provide an option to read chat using text-to-speech.

.. seealso::

    The `Game accessibility guidelines <https://gameaccessibilityguidelines.com/>`__ website contains a list of recommended features to create an accessible game.
