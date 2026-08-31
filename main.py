import os
import textwrap

WIDTH = 78

STORY = {
    'start': {
        'title': 'LAST SEEN',
        'text': [
            'The door closes.',
            'Nara drops her school bag beside the bed.',
            'She falls onto the mattress without taking off her uniform.',
            'Maya: “Nara! Go clean yourself up first!”',
            'Nara: “Yeah...”',
            'Nara looks at the ceiling. She just doesn’t know how to explain what she feels.',
            'BUP. Another notification.',
            'A community recommendation appears: CIRRUS — 37 members • 4 online.'
        ],
        'choices': [('Enter CIRRUS', 'd1', {})]
    },
    'd1': {
        'title': 'DAY 1 — CIRRUS',
        'text': ['0xZERO: hey! welcome new fellow :D', 'Nara: hii..', 'lune: welcome nara!! :)', 'vale: Welcome to CIRRUS, Nara.', 'What does Nara do?'],
        'choices': [('Say something', 'd2', {'kyle_trust': 1}), ('Stay quiet and observe', 'd2', {})]
    },
    'd2': {
        'title': 'DAY 2 — LUNE’S GOSSIP',
        'text': ['lune: can I tell you something?', 'She tells Nara a rumor about someone from her old school and says she spread it because “people deserved to know.”', 'The conversation will affect Nara’s relationship with Lune.'],
        'choices': [('Listen to Lune', 'd3', {'lune_trust': 1, 'toxic_seen': True}), ('Say judging rumors is unfair', 'd3', {'lune_trust': -1, 'defended_someone': True, 'toxic_seen': True}), ('Change the subject', 'd3', {'ignored_warning': True, 'toxic_seen': True})]
    },
    'd3': {
        'title': 'DAY 3 — THE FIRST CRACK',
        'text': ['CIRRUS feels familiar now. Maybe too familiar.', 'Where does Nara look?'],
        'choices': [('Gaming', 'gaming', {'kyle_trust': 1}), ('Off-topic', 'offtopic', {'toxic_seen': True}), ('After-hours', 'afterhours', {'evidence': 1})]
    },
    'gaming': {
        'title': 'GAMING',
        'text': ['Kyle jokes about someone who is not online. Lune laughs. Nara hesitates.'],
        'choices': [('Laugh along', 'd4', {'kyle_trust': 1}), ('Don’t respond', 'd4', {'ignored_warning': True})]
    },
    'offtopic': {
        'title': 'OFF-TOPIC',
        'text': ['Rumors about someone who is not in the channel fill the chat.'],
        'choices': [('Ask them to stop', 'd4', {'defended_someone': True, 'evidence': 1}), ('Scroll past', 'd4', {'ignored_warning': True})]
    },
    'afterhours': {
        'title': 'AFTER-HOURS',
        'text': ['vale: Does anyone still remember Mika?', 'A few seconds later: [message deleted]', 'Nara takes a screenshot.'],
        'choices': [('Keep investigating', 'd4', {'mika_evidence': 1, 'evidence': 1})]
    },
    'd4': {
        'title': 'DAY 4 — MIKA',
        'text': ['Nara searches the server for one name: MIKA.', 'Old results show: “Can someone tell them to stop?” “I didn’t say that.” “Why is everyone talking about me?”', 'Some messages are unavailable.'],
        'choices': [('Open the old messages', 'lune', {'mika_evidence': 2, 'evidence': 1}), ('Close the search', 'lune', {'ignored_warning': True})]
    },
    'lune': {
        'title': 'DAY 4 — QUESTIONS',
        'text': ['Nara asks Lune who Mika was. Lune says: “Don’t dig into things that aren’t yours.”'],
        'choices': [('Ask what happened', 'd5', {'lune_trust': 1, 'evidence': 1}), ('Leave it alone', 'd5', {'ignored_warning': True})]
    },
    'd5': {
        'title': 'DAY 5 — VALE',
        'text': ['Vale messages privately: “You’ve been looking through old channels.”', '“Mika’s story is complicated. People make mistakes.”'],
        'choices': [('Trust Vale', 'd6', {'vale_trust': 1}), ('Ask how reports were handled', 'd6', {'evidence': 2, 'report_ready': True}), ('Take screenshots before replying', 'd6', {'evidence': 2, 'report_ready': True})]
    },
    'd6': {
        'title': 'DAY 6 — THE TRUTH',
        'text': ['Kyle warns Nara to stop asking about Mika.', '“Vale knows. And Lune knows more than she’s saying.”'],
        'choices': [('Ask Kyle for everything', 'final', {'kyle_trust': 1, 'evidence': 1}), ('Ask Lune directly', 'final', {'evidence': 3}), ('Go to the archive', 'final', {'evidence': 4, 'report_ready': True})]
    },
    'final': {
        'title': 'FINAL CHOICE',
        'text': ['Nara looks at the folder on her desktop: screenshots, messages, names. Enough to show this was not just one person’s mistake.'],
        'choices': [('Tell Maya everything', 'home', {}), ('Stay and confront everyone', 'mirror', {}), ('Delete everything and pretend nothing happened', 'silence', {})]
    },
    'home': {
        'title': 'ENDING: HOME',
        'text': ['Nara closes CIRRUS and tells Maya everything.', 'The next morning, the evidence is handed to the proper authorities.', 'Not everyone apologizes, but someone finally stopped looking away.', 'Some distances can only be crossed by speaking.'],
        'choices': [('Play again', 'start', {'__restart__': True}), ('Exit game', '__exit__', {})]
    },
    'mirror': {
        'title': 'ENDING: MIRROR',
        'text': ['Nara starts confronting people, then exposing them. Private messages become weapons.', 'She wanted to stop the cycle, but learns how easy it is to become part of it.', 'Stopping harm means refusing to pass it on.'],
        'choices': [('Play again', 'start', {'__restart__': True}), ('Exit game', '__exit__', {})]
    },
    'silence': {
        'title': 'ENDING: SILENCE',
        'text': ['Nara deletes the folder and closes the laptop. The server continues.', 'Another rumor begins. Another person stays silent.', 'Silence doesn’t end the cycle.'],
        'choices': [('Play again', 'start', {'__restart__': True}), ('Exit game', '__exit__', {})]
    }
}


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def new_state():
    return {
        'lune_trust': 0,
        'kyle_trust': 0,
        'vale_trust': 0,
        'evidence': 0,
        'mika_evidence': 0,
        'toxic_seen': False,
        'defended_someone': False,
        'ignored_warning': False,
        'report_ready': False,
    }


def print_wrapped(line=''):
    for paragraph in str(line).split('\n'):
        print(textwrap.fill(paragraph, WIDTH) if paragraph else '')


def show_node(node):
    data = STORY[node]
    clear()
    print('=' * WIDTH)
    print(data['title'].center(WIDTH))
    print('=' * WIDTH)
    print()
    for line in data['text']:
        print_wrapped(line)
        print()


def choose(choices):
    while True:
        for i, (label, _, _) in enumerate(choices, 1):
            print(f'[{i}] {label}')
        answer = input('\nChoose an option: ').strip()
        if answer.isdigit() and 1 <= int(answer) <= len(choices):
            return choices[int(answer) - 1]
        print('Please enter one of the numbers shown above.\n')


def apply_updates(state, updates):
    if updates.get('__restart__'):
        return new_state()
    for key, value in updates.items():
        if key not in state:
            continue
        if isinstance(value, int) and isinstance(state[key], int):
            state[key] += value
        else:
            state[key] = value
    return state


def main():
    state = new_state()
    node = 'start'

    while True:
        show_node(node)
        label, target, updates = choose(STORY[node]['choices'])

        if target == '__exit__':
            clear()
            print('\nThanks for playing LAST SEEN.\n')
            break

        state = apply_updates(state, updates)
        node = target


if __name__ == '__main__':
    main()
