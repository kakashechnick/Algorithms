def MyFunction(line_string: str):
  # noinspection PyBroadException
  try:
    return int(line_string)

  except Exception:
    return None


template = 'vika'
pleaseCount = 0
mainList = list()
# noinspection PyBroadException
try:
  iteration_value = int(input())

  if not 1 <= iteration_value <= 100:
    exit()  # замена print('NO') !!!

  for i in range(iteration_value):
    # noinspection PyBroadException
    try:
      string_format = input().split(' ')
      string_format = [x for x in list(map(MyFunction, string_format)) if x is not None]

      if not len(string_format) == 2:
        print(string_format)
        print('NO')   # замена exit() !!!

      else:
        extensions = ''

        for words in range(string_format[0]):
          extensions = input()

          if len(extensions) != string_format[1]:
            print('NO')
            continue

          mainList.append(extensions)

        for spaseColumn in range(string_format[1]):
          for spaseRow in range(string_format[0]):
            if template[pleaseCount] == mainList[spaseRow][spaseColumn]:
              pleaseCount += 1



        mainList.clear()

    except Exception:
      print('NO')   # замена exit() !!!

except Exception:
  exit()