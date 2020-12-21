import shedule, tg

def formatChanges(chg, grp):
    message = ""
    for change in chg[grp]:
        message += f"Пара №{change['num']} - {change['name']}\n"
    return message

bot = tg.Tg("ВАШ ТОКЕН", ИД ПОЛЬЗОВАТЕЛЯ/БЕСЕДЫ)

groups = ["21-ІП", "22-ІП", "23-ІП"]

myshedule = shedule.Shedule("page.html", True)
oldchanges = myshedule.getGroupsChanges(groups)

txt = ""
for group in oldchanges:
    txt += f"Группа: {group}\nИзменения:\n"+formatChanges(oldchanges, group)
bot.say("Бот запущен. Текущие состояния:\n"+txt)

while True:
    try:
        myshedule.update()
        changes = myshedule.getGroupsChanges(groups)

        if changes != oldchanges:
            message = ""
            for group in changes:
                if changes[group] != oldchanges[group]:
                    message += f"=============\nОбнаружены изменения в группе {group}:\n"
                    message += formatChanges(changes, group)
                    bot.say(message)
            
            oldchanges = changes

    except KeyboardInterrupt:
        print("Ок, завершаем")
        quit()
