Database Backend
==========================

| New in version 1.6.0 you could change the database backend to postgres.
| You do that by adding this section to the configuration file (or use environment variables).

.. code-block:: yaml

    backend:
      type: postgres
      postgres:
        host: 127.0.0.1
        port: 5439
        user: postgres
        password: postgres

Please make sure when you do, to make sure you don't open the database to the world. Keep it secure.


Turoial
-------------

.. raw:: html

    <iframe width="560" height="315" src="https://www.youtube.com/embed/1t54UJRHYvM" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>