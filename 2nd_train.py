import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.train_mnt_encoder import *

if __name__ == "__main__":
    # Set random seed
    random_seed = 1
    torch.manual_seed(random_seed)
    random.seed(random_seed)

    opts = MntEncoderTrainOptions().parse()
    if os.path.exists(opts.exp_dir):
        if len(os.listdir(opts.exp_dir)) > 1:
            ans = input(
                "Oops... {} already exists. Do you wish to continue training_utils? [yes/no] ".format(
                    opts.exp_dir
                )
            )
            if ans == "no":
                raise Exception(
                    "stop training_utils! Please change exp_dir argument.".format(
                        opts.exp_dir
                    )
                )

    else:
        os.makedirs(opts.exp_dir)

    opts_dict = vars(opts)
    pprint.pprint(opts_dict)
    with open(os.path.join(opts.exp_dir, "opt.json"), "w") as f:
        json.dump(opts_dict, f, indent=4, sort_keys=True)

    coach = MntEncoderCoach(opts)
    coach.train()
