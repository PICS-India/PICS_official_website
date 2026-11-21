// Central place for links you still need to fill in.
// Leave a value as '' to hide/redirect it until the real URL is available.

export const SITE = {
  name: 'PICS',
  fullName: 'Policy Impact Challenge Series',
  organisation: 'The Indian Netizens',
  // External registration form (Google Form, Typeform, etc.).
  // When empty, "Register" buttons scroll to the registration banner on the home page.
  registrationUrl: '',
  linkedinUrl: '',
  contactEmail: '',
};

/** Props for a <Button> that should take people to registration. */
export function registerLinkProps() {
  return SITE.registrationUrl
    ? { href: SITE.registrationUrl, target: '_blank', rel: 'noopener noreferrer' }
    : { to: '/#register' };
}
