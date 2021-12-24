test = {
  'name': 'Veritasiness',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> True and 13
          72c74b6c7ed80d51f9fa7defbf7ed121
          # locked
          >>> False or 0
          b0754f6baafe74512d1be0bd5c8098ed
          # locked
          >>> not 10
          5dfeeb9ca37d955606d40c6553cd4956
          # locked
          >>> not None
          5154670fa295caf18cafa4245c1358a9
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> True and 1 / 0 and False  # If this errors, just type Error.
          d7b5fd49f83e4ee318af207fc969c9f4
          # locked
          >>> True or 1 / 0 or False  # If this errors, just type Error.
          5154670fa295caf18cafa4245c1358a9
          # locked
          >>> True and 0  # If this errors, just type Error.
          b0754f6baafe74512d1be0bd5c8098ed
          # locked
          >>> False or 1  # If this errors, just type Error.
          f26f9ec9ba426ebfdd8a43b22c8c74a0
          # locked
          >>> 1 and 3 and 6 and 10 and 15  # If this errors, just type Error.
          438f344a520081fe8e2d0da944a5240b
          # locked
          >>> -1 and 1 > 0 # If this errors, just type Error.
          5154670fa295caf18cafa4245c1358a9
          # locked
          >>> 0 or False or 2 or 1 / 0  # If this errors, just type Error.
          6d6f378f0affa7f84aa38e519e353617
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> not 0
          5154670fa295caf18cafa4245c1358a9
          # locked
          >>> (1 + 1) and 1  # If this errors, just type Error. If this is blank, just type Nothing.
          f26f9ec9ba426ebfdd8a43b22c8c74a0
          # locked
          >>> 1/0 or True  # If this errors, just type Error. If this is blank, just type Nothing.
          d7b5fd49f83e4ee318af207fc969c9f4
          # locked
          >>> (True or False) and False  # If this errors, just type Error. If this is blank, just type Nothing.
          5dfeeb9ca37d955606d40c6553cd4956
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
