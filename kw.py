def print_score(**kw):
    print('    Name Score')
    print('---------')
    for name, score in kw.items():
        print('%10s  %d' % (name, score))
    print()

print_score(Adama=99, Lisa=88, Bart=77)

data={'Adama Lee': 99,
      'Lisa S': 88,
      'F.Bart': 77
    }
print_score(**data)

def print_info(name, *, gender, city='Beijing', age):
    print('Personal Info')
    print('--------------')
    print('  Name: %s' % name)
    print('  Gender: %s' % gender)
    print('  City: %s' % city)
    print('  Age: %d' % age)
    print()

print_info('Bob', gender='male', age=20)
print_info('Lisa', gender='female', city='Hubei', age=18)
    
