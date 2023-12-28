from flask import Flask, redirect, render_template,request, url_for
import sqlite3

app = Flask(__name__)

DATABASE = 'database.db'

def connect_db():
    return sqlite3.connect(DATABASE)


@app.route('/')
def index():
    db = connect_db()
    
    db.execute('''
        CREATE TABLE IF NOT EXISTS product (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name TEXT NOT NULL,
            product_details TEXT NOT NULL,
            price REAL NOT NULL,
            ImageURL TEXT
        )
    ''')

    db.execute('DELETE FROM product')

    db.execute('''
        INSERT INTO product (product_name, product_details, price, ImageURL) VALUES
            ('Çorap', 'Kadın, Çorap', 19.99, 'https://cdn.dsmcdn.com/ty639/product/media/images/20221212/18/235058945/646895416/1/1_org.jpg'),
            ('Eşofman Altı', 'Kadın, Eşofman Altı', 29.99, 'https://cdn.dsmcdn.com/ty1014/product/media/images/prod/SPM/PIM/20231015/17/387a2e74-6fc5-344d-a54d-bf60b32b951b/1_org_zoom.jpg'),
            ('Gecelik', 'Kadın, Siyah Gecelik', 39.99, 'https://cdn.dsmcdn.com/ty712/product/media/images/20230203/15/272837558/212232897/1/1_org_zoom.jpg'),
            ('Gecelik', 'Kadın, Mavi Gecelik', 49.99, 'https://cdn.dsmcdn.com/ty952/product/media/images/20230616/10/386098658/581243875/1/1_org_zoom.jpg'),
            ('Playstation 5', 'PS5, Oyun Konsolu', 400.99, 'https://cdn.dsmcdn.com/ty78/product/media/images/20210226/14/67166691/129750724/1/1_org_zoom.jpg'),
            ('Pantalon', 'Kadın, Siyah Pantalon', 69.99, 'https://cdn.dsmcdn.com/ty1009/product/media/images/prod/SPM/PIM/20231005/15/827227af-1a7d-343f-b893-940ace69b97b/1_org_zoom.jpg'),
            ('Ceket', 'Kadın, Siyah-Beyaz Ceket', 79.99, 'https://cdn.dsmcdn.com/ty1003/product/media/images/prod/SPM/PIM/20230925/19/9d3963eb-8277-3684-a398-5483a33eb5b2/1_org_zoom.jpg'),
            ('Kazak', 'Kadın, Renkli Kazak', 89.99, 'https://cdn.dsmcdn.com/ty997/product/media/images/prod/SPM/PIM/20230910/18/15cf47eb-9c97-369c-a343-a2c9391fb6c5/1_org_zoom.jpg'),
            ('Parfüm', 'Kadın, Burberry Classic Parfüm', 99.99, 'https://cdn.dsmcdn.com/ty179/product/media/images/20210920/10/133806806/246558127/1/1_org_zoom.jpg'),
            ('Parfüm', 'Kadın, Burberry Her Parfüm', 109.99, 'https://cdn.dsmcdn.com/ty669/product/media/images/20221230/13/249332766/17791771/1/1_org_zoom.jpg')
    ''')

    db.commit()

    cursor = db.execute('SELECT * FROM product')

    products = cursor.fetchall()

    db.close()

    return render_template('index.html', products=products)

@app.route('/detail/<int:product_id>')
def detail(product_id):
    db = connect_db()
    cursor = db.execute('SELECT * FROM product WHERE id = ?', (product_id,))
    product = cursor.fetchone()
    db.close()
    return render_template('detail.html', product=product)

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_query = request.form.get('search_query')

        db = connect_db()
        cursor = db.execute('SELECT * FROM product WHERE product_name LIKE ? ', ('%' + search_query + '%',))
        cursor = db.execute('SELECT * FROM product WHERE product_details LIKE ? ', ('%' + search_query + '%',))
        search_results = cursor.fetchall()
        db.close()

        return render_template('search.html', search_results=search_results)

if __name__ == '__main__':
    app.run(debug=True, port=5001)




