Echo VR API Reference
=====================

The primary entry point of the API is through the :meth:`.fetch_state` method.
This method returns a :class:`~.GameState` object which you can then traverse
to find any information you could want.

If for some reason you need more direct control over how the API is accessed,
you may instead decide to use the :class:`~.API` class directly.

Installation
------------

If you haven't already, first `install Python 3`_ and `Pipenv`_.

.. _install Python 3: https://www.python.org/downloads/
.. _Pipenv: https://pipenv.readthedocs.io/en/latest/install/

Now, in your project directory, run::

    pipenv install echovr-api


Basic Usage
-----------

Example::

    import echovr_api

    try:
        game_state = echovr_api.fetch_state()

        print(f"Game status: {game_state.game_status}")
        print(f"Seconds on clock: {game_state.game_clock}")
        print(f"Score: {game_state.blue_team.score} - {game_state.orange_team.score}")

        # See `GameState` reference for available properties/methods
    except ConnectionError as e:
        # Echo VR is not running, or you didn't pass the -http parameter when
        # starting it.
    except json.decoder.JSONDecodeError as e:
        # Echo VR is currently not in an Arena match

Reference
---------

For a complete listing of available modules, classes, and methods, see
:ref:`modindex`.

You can also view comprehensive documentation of the raw HTTP API itself at the
`Unofficial Echo VR API Documentation`__.

__ https://github.com/Ajedi32/echovr_api_docs
