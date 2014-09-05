#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Asks the great question."""


the_great_question = ('Michaelangelo. Leonardo. Rafael. Donatello. Turtles? '
                      'Creators of the great works? Both? You be the judge!')
statements = the_great_question.split('. ')
artists = statements[0:4]

num_artists = len(artists) #4
characters = len(the_great_question) #105

has_creators = 'Creator' in the_great_question #returns true
has_splinter = 'Splinter' in artists #returns false