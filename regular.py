import re, argparse, unicodedata, string

def filter(inputName, outputName):
    outputFile = open(outputName, 'w')
    for line in open(inputName, 'r'):
        line = line.rstrip('\n')
        result = unicodedata.normalize('NFKC',line)  #fullwidth to half-width 
        #note: need to filter english and its POS
        result = re.sub(r'\((A|Caa|Cab|Cba|Cbb|D|DE|Da|Dfa|Dfb|Di|Dk)\)','',result)
        result = re.sub(r'\s+\S+\((FW)\)|\s+\((FW)\)','',result)
        result = re.sub(r'\((|I|Na|Nb|Nc|Ncd|Nd|Nep|Neqa|Neqb|Nes|Neu)\)','',result)
        result = re.sub(r'\((Nf|Ng|Nh|Nv|P|SHI|T|VA|VAC|VB|VC|VCL|VD|VE)\)','',result)
        result = re.sub(r'\((VF|VG|VH|VHC|VI|VJ|VK|VL|V\_2)\)','',result)
        result = re.sub(r'[\-]{130}','',result)
        result = re.sub(r'\s\S+\((COLONCATEGORY)\)','',result)
        result = re.sub(r'\s\S+\((COMMACATEGORY)\)','',result)
        result = re.sub(r'\s\S+\((DASHCATEGORY)\)','',result)
        result = re.sub(r'\s\S+\((ETCCATEGORY)\)','',result)
        result = re.sub(r'\s\S+\((EXCLAMATIONCATEGORY)\)','',result)
        result = re.sub(r'\s\S+\((PARENTHESISCATEGORY)\)','',result)
        result = re.sub(r'\s\S+\((PAUSECATEGORY)\)','',result)
        result = re.sub(r'\s\S+\((PERIODCATEGORY)\)','',result)
        result = re.sub(r'\s\S+\((QUESTIONCATEGORY)\)','',result)
        result = re.sub(r'\s\S+\((SEMICOLONCATEGORY)\)','',result)
        result = re.sub(r'\s\S+\((SPCHANGECATEGORY)\)','',result)
        if not result.strip():
                continue
        else:
            outputFile.write(result)
            outputFile.write(' \n')
    outputFile.close()

if __name__ == '__main__':
    #command parser
    parser = argparse.ArgumentParser( \
        description="format the trainingData for the input of the mglda.py program.", \
        epilog="Example: python3 regular.py smallTrainingData.txt smallTrainingData.final.txt")
    parser.add_argument("inputFile", help="the inputFile to process")
    parser.add_argument("outputFile", help="the outputFile to construct")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-q","--quiet",help="show nothing",action="store_true")
    group.add_argument("-d","--detail", help="show the detail setting messages", action="store_true")
    args = parser.parse_args()
    #program message
    if args.detail:
        print('Processing inputFile: {} and contruct outputFile: {}'.format(args.inputFile, args.outputFile))
    elif args.quiet:
        print()
    else:
        print('Running {} '.format(__file__))

    #algorithm
    filter(args.inputFile, args.outputFile)

