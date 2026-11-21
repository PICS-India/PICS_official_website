function Logo({ className = '' }) {
  return (
    <span className={`logo ${className}`.trim()}>
      PICS<b aria-hidden="true">|</b>
    </span>
  );
}

export default Logo;
