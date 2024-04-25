import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.inference_generator import *

if __name__ == "__main__":
    # Set random seed
    random_seed = 1
    torch.manual_seed(random_seed)
    random.seed(random_seed)

    device = "cuda"

    run()