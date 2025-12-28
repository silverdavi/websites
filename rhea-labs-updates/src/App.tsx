import styles from './App.module.css'

function App() {
  return (
    <div className={styles.app}>
      {/* ═══════════════════════════════════════════════════════════════════
          HERO
          ═══════════════════════════════════════════════════════════════════ */}
      <section className={styles.hero}>
        <div className={styles.heroContent}>
          <h1 className={styles.title}>Rhea Labs Updates</h1>
          <p className={styles.subtitle}>Coming soon...</p>
        </div>
      </section>
    </div>
  )
}

export default App

