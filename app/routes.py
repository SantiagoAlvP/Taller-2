from flask import render_template, jsonify
import random
import boto3
from app.models import pokeneas
from app import app
from config import Config

s3 = boto3.client(
    's3',
    aws_access_key_id=Config.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=Config.AWS_SECRET_ACCESS_KEY,
    region_name=Config.S3_REGION
)

@app.route('/')
def index():
    return "Bienvenido a la Pokédex de Pokeneas!"

@app.route('/pokenea/json')
def pokenea_json():
    pokenea = random.choice(pokeneas)
    container_id = open('/etc/hostname').read().strip()
    
    return jsonify({
        'id': pokenea.id,
        'nombre': pokenea.nombre,
        'altura': pokenea.altura,
        'habilidad': pokenea.habilidad,
        'container_id': container_id
    })

@app.route('/pokenea/html')
def pokenea_html():
    pokenea = random.choice(pokeneas)
    container_id = open('/etc/hostname').read().strip()
    
    # Generar URL firmada para la imagen
    image_url = s3.generate_presigned_url(
        'get_object',
        Params={'Bucket': Config.S3_BUCKET, 'Key': pokenea.imagen},
        ExpiresIn=3600
    )
    
    return render_template('pokenea.html', 
                        imagen=image_url, 
                        frase=pokenea.frase,
                        container_id=container_id)

