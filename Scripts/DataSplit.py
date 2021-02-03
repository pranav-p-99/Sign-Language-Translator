import splitfolders

splitfolders.ratio("..\Data", output="..\DataSplit", seed=1337,
                   ratio=(.8, .2), group_prefix=None)
