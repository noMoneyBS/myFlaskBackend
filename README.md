## PS
Not working as expected, because openai api is not able to generate text from image...


## Usage

```bash

$ pip install -r requirements.txt
$ export OPENAI_API_KEY= <your openai api key>
$ python run.py

```

## Project Structure

```bash

/back_end/
│
├── /app/                   
│   ├── /routes/             
│   │   └── image_routes.py  
│   ├── /services/           
│   │   └── openai_service.py
│   ├── /utils/              
│   │   └── image_utils.py   
│   └── __init__.py          
│
├── /uploads/                
│
├── config.py                
├── run.py                   
├── requirements.txt         
└── README.md                

```