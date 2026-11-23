# Урок 5 — расследование по истории

1. Всего коммитов: 13
   Команда: `git log --oneline | wc -l`
2. Первый коммит: `2ba938e` — docs: add project documents
   Команда: `git log --oneline | tail -1`
3. Раздел урока 4 в глоссарии: коммит `f9aec8e`, первый термин — input (ввод)
   Команды: `git log --oneline -- GLOSSARY.md`, `git show f9aec8e -- GLOSSARY.md`