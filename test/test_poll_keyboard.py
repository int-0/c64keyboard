#!/usr/bin/env python
#
# -*- coding: utf-8 -*-
#
# Note:
# This programs **MUST** be executed with root permissions
#

import RPi.GPIO as GPIO

_COLUMNS_PINS = [3, 5, 7, 11, 13, 15, 19, 21]
_ROWS_PINS = [8, 10, 12, 16, 18, 22, 23, 24, 26]

KEYS = {
    3:{
        8: 'RESTORE',
        10: '2',
        12: 'Q',
        16: 'COMMODORE',
        18: 'SPACE',
        22: 'RUN_STOP',
        23: '1',
        24: 'CTRL',
        26: 'BACKSPACE'
    },
    5:{
        8: None,
        10: '4',
        12: 'E',
        16: 'S',
        18: 'Z',
        22: 'L_SHIFT',
        23: '3',
        24: 'A',
        26: 'W'
    },
    7:{
        8: None,
        10: '6',
        12: 'T',
        16: 'F',
        18: 'C',
        22: 'X',
        23: '5',
        24: 'D',
        26: 'R'
    },
    11:{
        8: None,
        10: '8',
        12: 'U',
        16: 'H',
        18: 'B',
        22: 'V',
        23: '7',
        24: 'G',
        26: 'Y'
    },
    13:{
        8: None,
        10: '0',
        12: 'O',
        16: 'K',
        18: 'M',
        22: 'N',
        23: '9',
        24: 'J',
        26: 'I'
    },
    15:{
        8: None,
        10: '-',
        12: '@',
        16: ':',
        18: '.',
        22: ',',
        23: '+',
        24: 'L',
        26: 'P'
    },
    19:{
        8: None,
        10: 'CLR_HOME',
        12: 'UP',
        16: '=',
        18: 'R_SHIFT',
        22: '/',
        23: 'GBP',
        24: ';',
        26: '*'
    },
    21:{
        8: None,
        10: 'F7',
        12: 'F5',
        16: 'F3',
        18: 'F1',
        22: 'CRSR_H',
        23: 'INST_DEL',
        24: 'CRSR_V',
        26: 'RETURN'
    }
}

def setup_gpio():
    GPIO.setwarnings(False)
    # Use pin numbers instead of names
    GPIO.setmode(GPIO.BOARD)
    # GPIO pins assigned to COLUMNS configured for output and set to low level
    GPIO.setup(_COLUMNS_PINS, GPIO.OUT)
    GPIO.output(_COLUMNS_PINS, GPIO.LOW)
    # GPIO pins assigned to ROWS configured for input with built-in pull down
    GPIO.setup(_ROWS_PINS, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def gpio_clean():
    GPIO.cleanup()

def scan():
    value = []
    for column in _COLUMNS_PINS:
        # Check this column: set to high level
        GPIO.output(column, GPIO.HIGH)
        for row in _ROWS_PINS:
            # RESTORE key is connected to every columns, so we can check
            # only the first one.
            if column != _COLUMNS_PINS[0] and row == _ROWS_PINS[0]:
                # Only check first line of RESTORE (is conected to all cols.)
                continue
            # Check every row for this column
            if GPIO.input(row) == GPIO.HIGH:
                # Key pressed!
                value.append(KEYS[column][row])
        # The column was checked, put line to low level again
        GPIO.output(column, GPIO.LOW)
    # Return all detected keys
    return value

    
if __name__ == '__main__':
    print 'This program must be executed with root permissions'
    print 'Initializing GPIO...',
    setup_gpio()
    print 'OK'

    try:
        while True:
            values = scan()
            for key in values:
                if not key:
                    continue
                # Show keys
                print key,
    except KeyboardInterrupt:
        print 'End scanning!'
    finally:
        print 'Quitting...',
        gpio_clean()
        print 'OK'
