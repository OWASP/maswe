---
title: Sensitive Data Not Removed After Use
id: MASWE-0118
alias: data-minimisation
platform: [android, ios]
profiles: [P]
mappings:
  masvs-v2: [MASVS-PRIVACY-1]

refs:
  - https://mas.owasp.org/MASTG/knowledge/android/MASVS-PLATFORM/MASTG-KNOW-0018/#webviews-cleanup
  - https://developer.android.com/privacy-and-security/security-tips?hl=en#WebView
  - https://developer.apple.com/documentation/webkit/wkwebsitedatastore
draft:
  description: |
    Applying data minimisation, including appropriate cleanup in the end of the lifecycle is important.

    1. Clear web state or prefer non-persistent web stores

    - Android:
        - `CookieManager.getInstance().removeAllCookies(ValueCallback<Boolean>)`
        - `WebStorage.getInstance().deleteAllData()`
        - `WebViewDatabase.getInstance(context).clearHttpAuthUsernamePassword()`

    - iOS:
        - `WKWebsiteDataStore.default().removeData(ofTypes: WKWebsiteDataStore.allWebsiteDataTypes(), modifiedSince: Date.distantPast)`
        - Use `WKWebsiteDataStore.nonPersistent()` for private sessions
        - `HTTPCookieStorage.shared.removeCookies(since: .distantPast)`
        - Use `WKHTTPCookieStore` for targeted cookie deletion

    2. Clear app cache and files

    - Android:
        - `context.cacheDir.deleteRecursively()`
        - `context.filesDir.deleteRecursively()`
        - `context.deleteDatabase(name)` for temporary databases
        - `SharedPreferences.edit().clear().apply()` to remove tokens or user data

    - iOS:
        - Remove items in `NSTemporaryDirectory()` and the Caches folder using `FileManager.default.removeItem(at:)`
        - For Core Data, call `NSPersistentStoreCoordinator.destroyPersistentStore(at:ofType:options:)` for a full wipe
        - Reset `UserDefaults` with `removePersistentDomain(forName:)`

    3. Avoid network caches

    - Android:
        - `HttpResponseCache.getInstalled()?.delete()` for legacy stack
        - For OkHttp: `okHttpClient.cache?.evictAll()` or disable caching with `CacheControl.FORCE_NETWORK`

    - iOS:
        - `URLCache.shared.removeAllCachedResponses()`
        - Disable caching via `URLSessionConfiguration.urlCache = nil` or set `requestCachePolicy = .reloadIgnoringLocalCacheData`
        - `URLSession.invalidateAndCancel()` to clear in-memory session state

  topics:
    - webview
    - webview-cleanup
    - caches
    - data-minimisation
    - cleanup
status: placeholder

---
