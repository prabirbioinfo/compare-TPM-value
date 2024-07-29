# Define two dictionaries to store the TPM values for each gene
gene_tpm_1 = {}
gene_tpm_2 = {}

# Define a list to store the genes with different TPM values
different_genes = []

# Replace the following data with your actual data
gene_names = ["gene1", "gene2", "gene3", "gene4", "gene5"]
tpm_values_1 = [10.5, 12.3, 8.7, 15.2, 9.1]
tpm_values_2 = [11.2, 13.1, 8.9, 14.8, 9.5]

# Add data to the dictionaries
for i in range(len(gene_names)):
    gene_tpm_1[gene_names[i]] = tpm_values_1[i]
    gene_tpm_2[gene_names[i]] = tpm_values_2[i]

# Check for differences in TPM values
for gene in gene_tpm_1:
    if gene_tpm_1[gene] != gene_tpm_2[gene]:
        different_genes.append((gene, gene_tpm_1[gene], gene_tpm_2[gene]))

# Write the genes with different TPM values to a file
with open("different_genes.txt", "w") as f:
    f.write("Genes with different TPM values:\n")
    for gene, tpm1, tpm2 in different_genes:
        f.write(f"Gene: {gene}\tTPM1: {tpm1}\tTPM2: {tpm2}\n")

# Print a message to the user
if different_genes:
    print("Genes with different TPM values have been saved to different_genes.txt")
else:
    print("No genes with different TPM values found.")
