from options.test_options import TestOptions
from data import DataLoader #genial
from models import create_model
from util.writer import Writer


def run_test(epoch=-1):
    print('Running Test')
    opt = TestOptions().parse()
    #print(opt)
    opt.serial_batches = True  # no shuffle

    
    dataset = DataLoader(opt)

    print("dataset")
    #print(dataset.__dict__)
    #print(str(dataset.opt.paths[0]))

    print("START CREATING THE MODEL")
    model = create_model(opt)
    print("FINISH CREATING THE MODEL");

    writer = Writer(opt)
    # test
    writer.reset_counter()
    #print("DATASET")
    #print(enumerate(dataset))
  

    f = open("/home/jeff/classification.txt", "w")

    for i, data in enumerate(dataset):
        #print("GET ITEM MODEL")
        #print("BATCH "+str(i))
        #print(data['mesh'][0])
        
        #print(data)
        #print("EDGES FEATURES")
        #print(data['edge_features'])
        #print(len(data['edge_features'][0]))
        #print(data['label'])



        #print(data['label'])
        
        model.set_input(data)
        #print("sera1")
        ncorrect, nexamples ,pred_class = model.test()

        #print("LABEL-CLASS")
        #print(str(dataset.opt.paths))
        
        #print("PREDIC-CLASS")
        #print(str(pred_class))

     
        #f.write("LABEL CLASS \n")
        #f.write(str(dataset.opt.paths))
        #for path in dataset.opt.paths:
        #    f.write(str(path)+"\n")

        #f.write("\n")
        #f.write("PREDIC CLASS\n")
        #f.write(str(pred_class)+"\n")
        
        for i in range(len(pred_class)):
            path,idclass = dataset.opt.paths[i]
            #print("path: "+ str(path))
            list_path = path.split("/")
            tam = len(list_path)
            new_path = "/"+list_path[tam-3]+"/"+list_path[tam-2]+"/"+list_path[tam-1]

            f.write(new_path+";"+dataset.opt.classes[pred_class[i]]+"\n")
        #for pred in pred_class:
        #    f.write()
            #f.write(str(pred.item())+"\n")

        


        
        writer.update_counter(ncorrect, nexamples)
    writer.print_acc(epoch, writer.acc)
    f.close()

    return writer.acc


if __name__ == '__main__':
    run_test()
