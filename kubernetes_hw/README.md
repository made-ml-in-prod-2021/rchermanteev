# Домашнее задание 3.

### Чек-лист:
```
0) Установил kubectl
1) Развернул kubernetes локально (https://kind.sigs.k8s.io/docs/user/quick-start/) (5 баллов)
2) Написал pod manifests(online-inference-pod.yaml), за основу взял образ из дз2 (4 баллов)
2а) Прописал requests/limits (online-inference-pod-resources.yaml) (2 баллов)
3) Использовал для выполнения образ из туториала k8s. Добавил liveness и readiness пробы (online-inference-pod-probes.yaml) (3 балла)
4) Создал replicaset и попробовал разные сценарии (online-inference-replicaset.yaml) (3 баллов)
5) Создал deployment
	а) Попробовал реализовать стратегию blue-green (online-inference-deployment-blue-green.yaml)
	б) Реализовал стратегию rolling-update (online-inference-deployment-rolling-update.yaml)
(3 балла)
9) Самооценку, провёл в этом чек-листе (1 - доп баллы)  

Всего: 21
```