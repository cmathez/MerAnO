import libsbml

### Step 1 : Get document and model

def read_sbml(file):
  """
  return model of SBML file 
  """
    document = libsbml.readSBML(file)
    if document.getNumErrors() > 0:
        print("Encountered the following SBML errors:" + "\n")
        document.printErrors()
    else:       
        return document
      
def get_model(document):
  model = document.getModel()
  return model

## Step 2 : Define Id for one organism

# def get_Id_organism(model):
#    return Id

## Step 3 :  Get each object

# def get_ListOfFunctionDefinitions(model):
#   return ListOfFunctionDefinitions

# def get_ListOfUnitDefinitions(model):
#   return ListOfUnitDefinitions

# def get_ListOfCompartments(model):
#   return ListOfCompartments

# def get_listOfSpecies(model):
#   return listOfSpecies

# def get_ListOfParameters(model):
#   return ListOfParameters

# def get_ListOfReactions(model):
#   return ListOfReactions

## Step 4 : Modify Id in a model

# def modify_Id(model):
#   return model

## Step 5 : Create new SBML to merge all documents

# Object
# ListOfFunctionDefinitions, 
# ListOfUnitDefinitions, 
# ListOfCompartments, 
# ListOfSpecies, 
# ListOfParameters, 
# ListOfInitialAssignments, 
# ListOfRules, 
# ListOfConstraints, 
# ListOfReactions,
# ListOfEvents.
#