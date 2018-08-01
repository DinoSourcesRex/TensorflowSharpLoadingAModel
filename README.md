# LoadingAModel with TensorFlowSharp

The model is generated using [Create.py](LoadingAModel/Create.py) and loaded [Load.py](LoadingAModel/Load.py). Both of these methods work with one another.

The [saved_model.pb](LoadingAModel/savepath/saved_model.pb) is already generated, if you want to re-generate it you will have to delete the savepath.

---

## Building

Make sure you're using x64 bit when compiling. [Program.cs](LoadingAModel/Program.cs) will fail on line 15 with an `Invalid GraphDef`.