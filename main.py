import torch
import argparse
from transformers import AutoModelForCausalLM, AutoTokenizer
import bitsandbytes as bnb

def quantize_model(model_name, quant_mode):
    print(f"Loading model: {model_name}")

    model = AutoModelForCausalLM.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    if quant_mode == "8bit":
        print("Applying 8-bit quantization...")
        model = AutoModelForCausalLM.from_pretrained(
            model_name, 
            load_in_8bit=True, 
            device_map="auto"
        )

    elif quant_mode == "4bit":
        print("Applying 4-bit quantization...")
        model = AutoModelForCausalLM.from_pretrained(
            model_name,
            load_in_4bit=True,
            device_map="auto"
        )

    else:
        print("Running model without quantization.")

    return model, tokenizer


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="NeuQuant - Model Quantization Tool")
    parser.add_argument("--model", type=str, required=True, help="Model name from Hugging Face")
    parser.add_argument("--mode", type=str, default="none", choices=["none", "8bit", "4bit"], help="Quantization mode")
    
    args = parser.parse_args()
    quantize_model(args.model, args.mode)
