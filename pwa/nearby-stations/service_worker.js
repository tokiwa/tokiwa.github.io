var CACHE_DYNAMIC_VERSION = 'dynamic-v1';
var CACHE_NAME = 'pwa-stations-caches';
var urlsToCache = [
    '/dashimaki929.github.io/pwa/nearby-stations/index.html',
    '/dashimaki929.github.io/data/json/stations.json',
];

self.addEventListener('install', function(event) {
    event.waitUntil(
        caches
            .open(CACHE_NAME)
            .then(function(cache) {
                return cache.addAll(urlsToCache);
            })
    );
});

self.addEventListener('fetch', event => {
    console.log('[Service Worker] Fetching something ...');
    event.respondWith(
        // キャッシュの存在チェック
        caches.match(event.request)
            .then(response => {
                if (response) {
                    return response;
                } else {
                    // キャッシュがなければリクエストを投げて、レスポンスをキャッシュに入れる
                    return fetch(event.request)
                        .then(res => {
                            return caches.open(CACHE_DYNAMIC_VERSION)
                                .then(cache => {
                                    // 最後に res を返せるように、ここでは clone() する必要がある
                                    cache.put(event.request.url, res.clone());
                                    return res;
                                })
                        })
                        .catch(() => {});
                }
            })
    );
});