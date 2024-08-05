from get_anchor_size import save_bar_chart

if __name__ == '__main__':
    print("test")
    img_categories = ['Image','person', 'stone', 'truck', 'excavator', 'car', 'shadow','cone','equipment','horse','column','bus']
    img_count = [54943,25388,24031,26173,13065,7220,1523,2670,3760, 322,2366,581]
    save_bar_chart('Class Distribution', 'Categories', 'Count@log', img_categories, img_count, scale='log', filename='Image_amount_distribution.png')

    pcd_categories = ['PCD','pickup','people','mining truck','excavator','semi-trailer truck','sedan','loader','medium truck']
    pcd_count = [22536,2482,24312,18450,2639,599,126882,53,8885]
    save_bar_chart('Class Distribution', 'Categories', 'Count@log', pcd_categories, pcd_count, scale='log', filename='PCD_amount_distribution.png')
