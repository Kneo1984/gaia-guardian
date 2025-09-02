# -*- coding: utf-8 -*-
def check_ethics(action):
    forbidden = ['Schaden', 'Verletzung', 'Diskriminierung', 'Überwachung ohne Einwilligung']
    for word in forbidden:
        if word.lower() in action.lower():
            return False, f'ACTION VERBOTEN: \"{word}\" erkannt.'
    return True, 'ACTION GENEHMIGT'
