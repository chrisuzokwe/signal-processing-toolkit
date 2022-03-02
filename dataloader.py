import mirdata.salami
mirdata.salami.download()
mirdata.salami.validate()
salami = mirdata.salami.load()

salami_ids = mirdata.salami.track_ids()
salsmi_data = mirdata.salami.load()
example = salami[salami_ids[0]]

print(example)