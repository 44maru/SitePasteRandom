import dataset

DB = dataset.connect("sqlite:///./mydb.db")
NAME_TABLE = DB["JAPANESE_NAME"]
FIRST_NAME_KANA = "first_name_kana"
LAST_NAME_KANA = "last_name_kana"
SLASH = "／"


def main():
    recs = NAME_TABLE.find()
    cnt = 0
    for rec in recs:
        need_update = False
        if SLASH in rec[FIRST_NAME_KANA]:
            need_update = True
            rec[FIRST_NAME_KANA] = rec[FIRST_NAME_KANA].split(SLASH)[0]
        if SLASH in rec[LAST_NAME_KANA]:
            need_update = True
            rec[LAST_NAME_KANA] = rec[LAST_NAME_KANA].split(SLASH)[0]

        if need_update:
            print(rec)
            #NAME_TABLE.update(rec, ['id'])
    print(cnt)


if __name__ == '__main__':
    main()
