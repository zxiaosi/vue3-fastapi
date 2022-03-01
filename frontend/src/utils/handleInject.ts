import { inject, type InjectionKey } from "vue";

/**
 * 为inject标注类型
 * @param key key值
 * @param fallback 失败返回信息
 * @returns inject(key)
 */
function injectStrict<T>(key: InjectionKey<T>, fallback?: T) {
  const resolved = inject(key, fallback);
  if (!resolved) {
    throw new Error(`Could not resolve ${key.toString}`);
  }
  return resolved;
}

export default injectStrict;
